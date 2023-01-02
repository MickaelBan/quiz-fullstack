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
    <ListScoreTop :maxlist="10"/>
    <div class="button">
      <input type="submit" value="Démarrer le quiz" v-on:click="newQuiz">
    </div>
  </body>
</template>


<script>
import ListScoreTop from "../components/ListScores.vue";

export default {
  name: "HomePage",
  components: {
    ListScoreTop
  },
  created() {
    console.log("Composant Home page 'created'");
  },
  methods:{
    newQuiz(){
      this.$router.push("/newQuiz")
    }
  }
};
</script>