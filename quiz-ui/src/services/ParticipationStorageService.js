export default {
    clear() {
        window.localStorage.clear()
    },
    savePlayerName(playerName) {
        window.localStorage.setItem("playerName", playerName);
    },
    getPlayerName() {		
        return window.localStorage.getItem("playerName")
    },
    saveParticipationScore(score){
        window.localStorage.setItem("score",score)
    },
    getParticipationScore(){
        return window.localStorage.getItem("score")
    }
  };