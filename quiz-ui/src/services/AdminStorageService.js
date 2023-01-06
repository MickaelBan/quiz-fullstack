export default {
  clear() {
    window.localStorage.removeItem("token")
  },
  savePlayerName(token) {
    window.localStorage.setItem("token", token);
  },
  getPlayerName() {
    return window.localStorage.getItem("token")
  }
};