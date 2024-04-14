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
