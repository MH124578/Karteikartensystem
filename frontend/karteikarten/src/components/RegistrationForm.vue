<template>
  <div>
    <h2>Registrierung</h2>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="Benutzername" />
      <input type="email" v-model="email" placeholder="E-Mail" />
      <input type="password" v-model="password" placeholder="Passwort" />
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
        console.log(response.data);
        // Weiterleitung oder Anzeige einer Erfolgsmeldung
      } catch (error) {
        // Überprüfe zuerst, ob error.response und error.response.data vorhanden sind
        if (error.response && error.response.data && error.response.data.detail) {
          console.error(error.response.data.detail);
        } else {
          // Allgemeiner Fehlerhandler, falls keine spezifischen Details vorhanden sind
          console.error("Ein Fehler ist aufgetreten.");
        }
      }
    },
  },
};
</script>

<style scoped>
.center {
  display: flex;
  justify-content: center;
  align-items: center;
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
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
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
