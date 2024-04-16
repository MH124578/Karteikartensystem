<template>
  <div id="app" class="app-container">
    <div v-if="isAuthenticated" class="content">
      <nav class="main-nav">
        <router-link to="/dashboard" class="nav-link">Dashboard</router-link>
        <router-link to="/create-flashcard" class="nav-link">Karteikarte erstellen</router-link>
        <router-link to="/create-category" class="nav-link">Kategorie erstellen</router-link>
        <button class="logout-button" @click="logout">Ausloggen</button>
      </nav>
      <router-view/>
    </div>
    <LoginForm v-else @login-success="isAuthenticated = true" class="login-form"/>
  </div>
</template>

<script>
import LoginForm from './components/LoginForm.vue';

export default {
  components: { LoginForm },
  data() {
    return { isAuthenticated: false };
  },
  created() {
    this.checkAuthStatus();
  },
  methods: {
    checkAuthStatus() {
      this.isAuthenticated = !!localStorage.getItem('user_id');
    },
    logout() {
      localStorage.removeItem('user_id');
      this.isAuthenticated = false;
      this.$router.push('/');
    }
  }
};
</script>

<style>
.app-container {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  background-color: #f7f8fa;
}

.content {
  text-align: center;
  padding: 10px;
}

.main-nav {
  background-color: #34495e;
  padding: 10px 0;
}

.nav-link {
  color: #ecf0f1;
  text-decoration: none;
  margin: 0 10px;
  padding: 5px 10px;
}

.nav-link:hover {
  background-color: #2c3e50;
  border-radius: 5px;
}

.logout-button {
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 5px 15px;
  border-radius: 5px;
  cursor: pointer;
}

.logout-button:hover {
  background-color: #c0392b;
}
</style>