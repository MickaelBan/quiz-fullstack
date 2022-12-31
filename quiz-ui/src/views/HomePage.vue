<style>
.title{
  padding: 20px;
  margin:30px;
  text-align: center
}
.list{
  padding: auto;
  text-align: center;
  padding: 20px;
}
.score{
  padding: 10px;
  margin: 5px;
  border-radius: 5px;
  background-color: #4CAF50;
  cursor: pointer;
  text-align: center;
}
.score:hover{
  background-color: #4CAF50;
  color: white;
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
}
.button{
  margin: 20px;
}
</style>
<template>
  <body>
    <div class="title">
      <h1>Home page</h1>
    </div>
    <div class="cpnt">      
      <h4>Top 10 of best player:</h4>
      <div class="list">
        <div v-for="(scoreEntry,index) in registeredScores" v-bind:key="scoreEntry.date" >
          <div v-if="index<10" class="score">
            {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
          </div>
        </div>
      </div>
    </div>
    <div class="button">
      <input type="submit" value="Démarrer le quiz" v-on:click="newQuiz">
    </div>
  </body>
</template>


<script>
import quizApiService from "@/services/QuizApiService";


export default {
  name: "HomePage",
  data() {
    let registeredScores = []
    return {
      registeredScores
    };
  },
  async created() {
    this.registeredScores = await quizApiService.getQuizInfo()
    this.registeredScores = this.registeredScores.data.scores
    console.log("Composant Home page 'created'");
  },
  methods:{
    newQuiz(){
      this.$router.push("/newQuiz")
    }
  }
};
</script>