<template>
  <div>
    <div class="card">
      <header class="card-header">
        <p class="card-header-title">
          {{ title }}
        </p>
        <a href="#" class="card-header-icon" aria-label="more options">
          <span class="icon">
            <i class="fas fa-angle-down" aria-hidden="true"></i>
          </span>
        </a>
      </header>
      <div class="card-image">
        <figure class="image">
          <img v-if="img" :src="img" />
          <img v-else src="https://cdn.shopify.com/s/files/1/0533/2089/files/placeholder-images-image_large.png?v=1530129081" alt="Placeholder image">
        </figure>
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
    img: String
  }
}
</script>

<style scoped>

</style>
