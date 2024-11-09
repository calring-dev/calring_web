<template>
  <div id="app">
    <!-- <vue-cal :events="events" view="month"></vue-cal> -->
    <vue-cal :events="events" is-view-changeable></vue-cal>
  </div>
</template>

<script>
import VueCal from 'vue-cal'
import 'vue-cal/dist/vuecal.css'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    VueCal
  },
  data() {
    return {
      events: []
    }
  },
  created() {
    axios.get('/api/events')
      .then(response => {
        this.events = response.data.map(event => ({
          title: event.event,
          start: event.date
        }))
      })
      .catch(error => {
        console.error(error)
      })
  }
}
</script>

<style>
</style>