<script setup>
import { RouterLink, RouterView } from 'vue-router';
import AdminStorageService from './services/AdminStorageService';

</script>

<template>
  <div class="app">
    <header>
      <div class="wrapper">
        <nav :key="$route.fullPath">
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/newQuiz">New Quiz</RouterLink>
          <RouterLink to="/scores">Scores</RouterLink>
          <div v-if="!AdminStorageService.isAdmin()">
            <RouterLink to="/login">Login</RouterLink>
          </div>
          <div v-else>
            <RouterLink to="/AdminSpace">admin space</RouterLink>
            <RouterLink to="/logout">Logout</RouterLink>
          </div>
        </nav>
      </div>
    </header>

    <body>
      <RouterView />
    </body>
  </div>
</template>

<style scoped>
.app {
  display: grid;
  place-items: center
}

header {
  line-height: 1.5;
  max-height: 100vh;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    /* display: flex; */
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }


  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    font-size: 1rem;
    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
