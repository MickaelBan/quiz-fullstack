
<template> 
    <div class="cpnt1">
      <h1>New quiz</h1>
    </div>

    <div class="cpnt1">
      <h3>Choose your name</h3>
    </div>

    <div class="cpnt">
      <label for="pName">Player Name</label>
      <input type="text" v-model="username" id="pName" name="playerName" placeholder="default" >
      <input id="pName" type="submit" value="launch quiz" v-if="username!=null" v-on:click="launchNewQuiz">
    </div>
</template>


<script>
import ParticipationStorageService from "../services/ParticipationStorageService";

export default {
  data(){
    let username = 'default'
    return {
      username
    }
  },
  created() {
    ParticipationStorageService.clear()
  },
  methods:{
    launchNewQuiz(){
      ParticipationStorageService.savePlayerName(this.username)
      console.log("save name")
      console.log("launch new quiz")
      this.$router.push('/questions');
    }
  }

}
</script>


