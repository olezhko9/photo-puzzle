<template>
  <div class="container">
    <div class="columns">
      <div class="column">
        <b-field>
        <b-upload v-model="file" class="is-info" drag-drop @input="onFileChange">
          <section class="section">
            <div class="has-text-centered">
              <p>
                <b-icon
                  icon="upload"
                  size="is-large">
                </b-icon>
               </p>
               <p>Перетащите сюда файл,</p>
               <p>который хотите обработать</p>
            </div>
          </section>
        </b-upload>
      </b-field>

        <div v-if="file" class="control">
          <b-tag
            type="is-primary"
            size="is-medium"
            @close="clearAll"
            attached closable>
            {{ file.name }}
          </b-tag>
          <b-button type="is-primary" @click="uploadImage">Отправить</b-button>
        </div>
    </div>

      <div class="column" id="preview">
        <img v-if="url" :src="url" />
        <img v-if="mosaicUrl" :src="mosaicUrl">
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Mosaic',
  data () {
    return {
      file: null,
      url: '',
      mosaicUrl: ''
    }
  },

  methods: {
    onFileChange (e) {
      this.url = URL.createObjectURL(this.file)
      this.mosaicUrl = ''
    },

    uploadImage () {
      let formData = new FormData()
      formData.append('file', this.file)
      axios.post('http://127.0.0.1:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(res => {
        this.mosaicUrl = 'http://127.0.0.1:5000/download/' + res.data.filename
      })
    },

    clearAll () {
      this.file = null
      this.url = ''
      this.mosaicUrl = ''
    }
  }
}
</script>

<style scoped>
#preview {
  display: flex;
  justify-content: center;
  align-items: center;
}

#preview img {
  max-width: 100%;
  max-height: 500px;
}
</style>
