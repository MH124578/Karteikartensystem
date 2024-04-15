<template>
    <div>
      <h2>Anmelden</h2>
      <form @submit.prevent="login">
        <input v-model="email" type="email" placeholder="E-Mail" required />
        <input v-model="password" type="password" placeholder="Passwort" required />
        <button type="submit">Anmelden</button>
      </form>
      <router-link to="/register" class="registration-link">Noch keinen Account? Hier Registrieren</router-link>
    </div>
    <router-view/>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        email: '',
        password: ''
      };
    },
    methods: {
        async login() {
        console.log("Sending:", this.email, this.password);
        try {
            const response = await axios.post('http://127.0.0.1:8000/login', {
            email: this.email,
            password: this.password,
            });
            console.log('Login successful:', response.data);
            localStorage.setItem('user_id', response.data.user_id);
            this.$emit('login-success');
            this.$router.push('/dashboard');
        } catch (error) {
            if (error.response && error.response.data && error.response.data.detail) {
            console.error('Fehler beim Anmelden:', error.response.data.detail);
            } else {
            console.error('Fehler beim Anmelden:', error);
            }
        }
        },
    }
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

input[type="email"], input[type="password"] {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #218838;
}
</style>
