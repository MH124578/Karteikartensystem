import { createRouter, createWebHistory } from 'vue-router';
import LoginForm from '@/components/LoginForm.vue';
import RegistrationForm from '@/components/RegistrationForm.vue';
import FlashcardCreationForm from '@/components/FlashcardCreationForm.vue';
import CategoryCreationForm from '@/components/CategoryCreationForm.vue';
import DashboardForm from '@/components/DashboardForm.vue';

const routes = [
  {
    path: '/',
    name: 'Login',
    component: LoginForm
  },
  {
    path: '/register',
    name: 'Register',
    component: RegistrationForm,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: '/create-flashcard',
    name: 'CreateFlashcard',
    component: FlashcardCreationForm,
  },
  {
    path: '/create-category',
    name: 'CreateCategory',
    component: CategoryCreationForm,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardForm
  },
  // Weitere Routen hier hinzufügen
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
