<template>
  <div class="container">
    <img src="/apple.png" alt="apple" width="100" height="100">
    <h1>Welcome to the Stock Data Dashboard</h1>
    <nuxt-link to="/login">
      <button>Login</button>
    </nuxt-link>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
}
</style>
