<style>
.title{
  padding: 50px;
  text-align: center
}
.list{
  padding: auto;
  text-align: center;
  padding: 2px;
}
.button{
  padding: 10px;
  text-align: center;
}
</style>
<template>
  <body>
    <div class="title">
      <h1>Home page</h1>
    </div>
    <div class="list" v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
      {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
    </div>
    <div class="button">
      <router-link  type="button" class="btn btn-dark" to="/start-new-quiz-page">Démarrer le quiz !</router-link>
    </div>
  </body>
</template>


<script>
import quizApiService from "@/services/QuizApiService";


export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: []
    };
  },
  async created() {
    this.registeredScores = await quizApiService.getQuizInfo()
    this.registeredScores = this.registeredScores.data.scores
    console.log("Composant Home page 'created'");
  }
};
</script>