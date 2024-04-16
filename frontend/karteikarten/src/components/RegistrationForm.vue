<template>
  <div class="center">
    <h2>Registrierung</h2>
    <form @submit.prevent="register">
      <input type="text" v-model="username" placeholder="Benutzername" required />
      <input type="email" v-model="email" placeholder="E-Mail" required />
      <input type="password" v-model="password" placeholder="Passwort" required />
      <button type="submit">Registrieren</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/create_users/', {
          username: this.username,
          email: this.email,
          password: this.password,
        });
        console.log("Registrierung erfolgreich:", response.data);
        // Implementiere Navigation nach erfolgreicher Registrierung
      } catch (error) {
        const errorMsg = error.response && error.response.data && error.response.data.detail
          ? error.response.data.detail
          : "Ein Fehler ist aufgetreten.";
        console.error(errorMsg);
      }
    },
  },
};
</script>

<style scoped>
.center {
  display: flex;
  flex-direction: column; /* Stellt die Elemente vertikal ein */
  justify-content: center; /* Zentriert die Elemente vertikal */
  align-items: center; /* Zentriert die Elemente horizontal */
  height: 100vh;
}

form {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  width: 300px;
}

input[type="text"], input[type="email"], input[type="password"] {
  width: calc(100% - 2px);
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>