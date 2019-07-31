<template>
  <div>
    <div class="card">
      <header class="card-header">
        <p class="card-header-title is-centered">
          {{ title }}
        </p>
      </header>
      <div class="card-image" :style="{'height': maxHeight + 'px'}">
        <img
          v-if="img"
          :src="img"
          @load="onImageLoaded"
          :style="{'max-height': maxHeight + 'px'}"
          crossorigin="anonymous"
          class="user-image" />
        <slot name="no-image" v-else />
      </div>
      <div class="card-content">
        <p class="title is-5 has-text-centered">{{ filename }}</p>
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
    maxHeight: Number,
    filename: String
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
    display: flex;
    align-items: center;
    justify-content: center
  }

  .card-image > .field {
    width: 100%;
    height: 100%;
  }

  .card-content > p {
    height: 22px;
  }

  footer.card-footer > a, footer.card-footer > button {
    height: 100%;
  }
</style>
