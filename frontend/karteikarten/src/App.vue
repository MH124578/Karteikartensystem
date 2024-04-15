<template>
  <div id="app">
    <!-- Zeige Navigationsleiste nur, wenn der Benutzer eingeloggt ist -->
    <div v-if="isAuthenticated">
      <nav>
        <router-link to="/dashboard">Dashboard</router-link> |
        <router-link to="/create-flashcard">Karteikarte erstellen</router-link> |
        <router-link to="/create-category">Kategorie erstellen</router-link>
      </nav>
      <router-view/>
    </div>
    <!-- Zeige Login-Formular, wenn der Benutzer nicht eingeloggt ist -->
    <LoginForm v-else @login-success="isAuthenticated = true"/>
  </div>
</template>

<script>
import LoginForm from './components/LoginForm.vue';

export default {
  components: {
    LoginForm
  },
  data() {
    return {
      isAuthenticated: false
    };
  }
};
</script>

<style>
#app {
  font-family: 'Arial', sans-serif;
  background-color: #f4f7f9;
}

nav {
  background-color: #007bff;
  color: white;
  padding: 10px;
  text-align: center;
}

nav a {
  color: white;
  text-decoration: none;
  margin: 0 15px;
}

nav a:hover {
  opacity: 0.8;
}
</style>
