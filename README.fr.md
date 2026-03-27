🌐 [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | Français | [Deutsch](README.de.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md) | [Türkçe](README.tr.md)

# Web Search Assistant

**Recherche web alimentée par l'IA utilisant l'API EvoLink**

Powered by [Evolink.ai](https://evolink.ai?utm_source=github&utm_medium=skill&utm_campaign=web-search)

Recherchez sur le web et obtenez des résultats propres et formatés avec titres, URLs et descriptions.

## 🚀 Démarrage rapide

```bash
bash scripts/search.sh "AI coding assistants 2026"
bash scripts/search.sh "quantum computing breakthroughs" 20
```

## 🔑 Configuration

Définissez votre clé API EvoLink :

```bash
export EVOLINK_API_KEY="your-evolink-api-key-here"
```

👉 [Obtenir une clé API gratuite](https://evolink.ai/signup?utm_source=github&utm_medium=skill&utm_campaign=web-search)

## 📖 Utilisation

### Recherche de base

```bash
bash scripts/search.sh "requête de recherche"
```

Renvoie les 10 meilleurs résultats.

### Limiter les résultats

```bash
bash scripts/search.sh "requête de recherche" 20
```

Spécifiez le nombre maximum de résultats.

## 🔒 Sécurité

**Identifiants et réseau**

`EVOLINK_API_KEY` est requis pour appeler l'API EvoLink. Vos requêtes de recherche sont envoyées à `api.evolink.ai` pour traitement. EvoLink gère la recherche web en interne et renvoie des résultats formatés.

**Accès aux fichiers**

Ce skill ne lit ni n'écrit de fichiers.

**Accès réseau**

Ce skill effectue des requêtes réseau vers :
- **API EvoLink** (`api.evolink.ai`) - pour effectuer des recherches web

Tous les appels réseau sont effectués via curl et peuvent être audités dans le code source du script.

**Persistance et privilèges**

Ce skill ne modifie pas d'autres skills ou paramètres système. Aucun privilège élevé ou persistant n'est demandé.

## 📄 Licence

MIT

## 🔗 Liens

- [ClawHub](https://clawhub.ai/evolinkai/web-research)
- [Référence API](https://docs.evolink.ai/en/api-manual/language-series/claude/claude-messages-api?utm_source=github&utm_medium=skill&utm_campaign=web-search)
- [Communauté](https://discord.com/invite/5mGHfA24kn)
- [Support](mailto:support@evolink.ai)
