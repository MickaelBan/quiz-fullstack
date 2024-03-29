# Récupération d'une image de base node JS 
# Notez le fait que cette "portion" est nommée "build"
FROM node:lts-alpine as build

# Installation du framework Vue
RUN npm install -g @vue/cli

# Création et positionnement du répertoire par défaut dans le container
WORKDIR /app

# Copie des fichiers référençant les dépendances de la machine hôte vers le container
# Ici, le répertoire cible est bien /app car il s'agit du WORKDIR
COPY package*.json ./

# Installation des dépendances
RUN npm install

# Copie du reste du code source
COPY . .

# En local même dans Docker, l'API sera toujours accessible comme lors des devs
# Important : pour déployer l'image de prod, nous changerons ce chemin en /api
ENV VITE_API_URL=http://localhost:5000

# Construction du bundle de l'application
# Ceci va générer la version de prod de l'UI dans le répertoire /app/dist
RUN npm run build

# La portion "build" de l'image est maintenant effectuée, nous n'avons plus besoin
# que de servir les fichiers qu'elle a générés. Pour cela nous utilison un serveur 
# Nginx dans lequel nous copions les fichiers générés par la portion "build"
FROM nginx as production-stage
COPY --from=build /app/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]