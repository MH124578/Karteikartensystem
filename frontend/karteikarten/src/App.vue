<template>
  <div id="app">
    <nav>
      <router-link to="/register">Registrieren</router-link> |
      <router-link to="/create-flashcard">Karteikarte erstellen</router-link> |
      <router-link to="/create-category">Kategorie erstellen</router-link>
    </nav>
    <router-view/>
  </div>
</template>
