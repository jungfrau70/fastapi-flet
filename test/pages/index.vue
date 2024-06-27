<template>
  <div>
    <Login />
    <nuxt-link to="/dashboard">Go to Dashboard</nuxt-link>
    <Tutorial />
  </div>
</template>

<script>
import Tutorial from '@/components/Tutorial.vue'
import Login from '@/components/Login.vue'

export default {
  name: 'IndexPage',
  components: {
    Tutorial,
    Login
  }
}
</script>
