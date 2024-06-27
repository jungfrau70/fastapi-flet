<template>
  <div class="container">
    <input v-model="username" placeholder="Username" />
    <input v-model="password" type="password" placeholder="Password" />
    <button @click="login">Login</button>
    <button @click="signup">Sign Up</button>
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      message: ''
    }
  },
  methods: {
    async login() {
      try {
        await this.$auth.loginWith('local', {
          data: {
            username: this.username,
            password: this.password
          }
        })
        this.$router.push('/dashboard')
      } catch (error) {
        this.message = 'Login failed'
      }
    },
    async signup() {
      try {
        await this.$axios.post('http://127.0.0.1:8000/signup', {
          username: this.username,
          password: this.password
        })
        this.message = 'Signup successful'
      } catch (error) {
        this.message = 'Signup failed'
      }
    }
  }
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
