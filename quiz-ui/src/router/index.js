import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsManager from '../components/QuestionsManager.vue'
import ScoresPage from '../views/ScoresPage.vue'
import Login from '../views/Login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/newQuiz',
      name: 'New Quiz',
      component: NewQuizPage
    },
    {
      path: '/questions',
      name: 'Quiz',
      component: QuestionsManager
    },
    {
      path: '/scores',
      name: 'Scores',
      component: ScoresPage
    },
    {
      path: '/login',
      name: 'Login', 
      component: Login
    }
  ]
})

export default router
