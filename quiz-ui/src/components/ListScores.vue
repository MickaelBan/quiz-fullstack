<template>
  <div class="cpnt">
    <div v-if="maxlist != null">
      <h4>Top {{ maxlist }} of best player:</h4>
      <div class="list">
        <div v-for="(scoreEntry, index) in registeredScores" v-bind:key="scoreEntry.date">
          <div v-if="index < maxlist" class="score">
            {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <h4>All classement:</h4>
      <div class="list">
        <div v-for="(scoreEntry, index) in registeredScores" v-bind:key="scoreEntry.date">
          <div class="score">
            {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
            <div v-if="playerName == scoreEntry.playerName & playerScore == scoreEntry.playerScore">
              {{ this.$emit('classement', index + 1) }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  props: {
    maxlist: {
      typeof: Number
    },
    playerName: { typeof: String },
    playerScore: { typeof: Number }
  },
  emits: ["classement"],
  data() {
    let registeredScores = []
    return {
      registeredScores
    };
  },
  async created() {
    this.registeredScores = await quizApiService.getQuizInfo()
    this.registeredScores = this.registeredScores.data.scores
    console.log("composant list of score");
  },
}
</script>