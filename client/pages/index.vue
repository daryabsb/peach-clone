<template>
  <div class="container">
  
    <b-card>
      <b-tabs v-model="tabIndex" card>
        <b-tab title="General">I'm the first fading tab</b-tab>
        <b-tab title="Edit profile">
          I'm the second tab
        </b-tab>
        <b-tab title="Premium Plan">Sibzamini!</b-tab>
        <b-tab title="Info">I'm the last tab</b-tab>
      </b-tabs>
    </b-card>
  </div>
</template>


<script>
  export default {
    data() {
      return {
        tabIndex: 1
      }
    }
  }
</script>