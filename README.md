# Pipeline Projekt

En liten Flask-app med en CI/CD-pipeline i GitHub Actions. När jag öppnar en pull request testas koden automatiskt, och när den mergas till main byggs en Docker image som pushas till GitHub Container Registry.

## Syfte

Jag ville lära mig hur CI/CD funkar på riktigt, hur man skyddar main och hur olika sorters tester passar in i en pipeline.

## Hur det fungerar

Main är skyddad så man kan inte pusha direkt. Allt går via pull requests och testerna måste vara gröna innan man får merga.

Pipelinen kör lint med ruff först eftersom det går snabbast, sen enhetstester med pytest. Efter det kommer ett integrationstest som bygger imagen, startar containern och anropar `/health` på riktigt.

När koden hamnar på main byggs imagen och pushas till ghcr.io, taggad med commit SHA så man vet exakt vilken kod den kommer från. Sist körs ett smoke test som hämtar den publicerade imagen och kollar att den svarar.

```
PR:    lint → test → integration
main:  lint → test → integration → build → smoke
```

## Teknik

* Flask
* pytest och ruff
* Docker
* GitHub Actions
* GitHub Container Registry

## Köra lokalt

```bash
pip install -r requirements-dev.txt
pytest
docker build -t pipeline-projekt .
docker run -p 5000:5000 pipeline-projekt
```

## Vad jag skulle göra bättre

* Bygga imagen en gång istället för två
* Använda en riktig produktionsserver istället för Flasks inbyggda
* Låsa versionerna i requirements
