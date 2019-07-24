<template>
  <div>
    <div class="card">
      <header class="card-header">
        <p class="card-header-title is-centered">
          {{ title }}
        </p>
      </header>
      <div class="card-image">
        <img
          v-if="img"
          :src="img"
          @load="onImageLoaded"
          :style="{'max-height': maxHeight + 'px'}"
          class="user-image" />
        <slot name="no-image" v-else />
      </div>
      <footer class="card-footer">
        <slot name="actions"/>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PhotoViewer',
  props: {
    title: String,
    img: String,
    maxHeight: Number
  },

  methods: {
    onImageLoaded () {
      this.$emit('imageLoaded')
    }
  }
}
</script>

<style scoped>
  .card-image {
    margin-top: 2px;
  }
</style>
