<template>
  <div class="title">
    <h1>Home page</h1>
  </div>
  <ListScoreTop :maxlist="10" />
  <div class="button">
    <input type="submit" value="Démarrer le quiz" v-on:click="newQuiz">
  </div>
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
  methods: {
    newQuiz() {
      this.$router.push("/newQuiz")
    }
  }
};
</script>