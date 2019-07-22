<template>
  <div class="container">
    <div class="columns">
      <div class="column is-one-quarter">
        <b-field>
          <b-upload
            v-model="file"
            type="is-primary"
            @input="onFileChange"
            accept="image/*"
            drag-drop>
            <section class="section">
              <div class="has-text-centered">
                <p>
                  <b-icon
                    icon="upload"
                    size="is-large">
                  </b-icon>
                </p>
                <p>Перетащите сюда файл, который хотите обработать</p>
              </div>
            </section>
          </b-upload>
        </b-field>

        <div v-if="file">
          <b-tag
            v-if="file"
            type="is-primary"
            size="is-medium"
            @close="clearAll"
            attached closable>
            {{ file.name }}
          </b-tag>
          <b-button
            type="is-primary"
            :class="{'is-loading': uploading}"
            @click="uploadImage">
            Отправить
          </b-button>
        </div>
       </div>

      <div class="column preview">
        <photo-viewer title="Оригинальная картинка" :img="url">
          <template slot="actions">
            <a href="#" class="card-footer-item">Close</a>
          </template>
        </photo-viewer>
      </div>

      <div class="column preview">
        <photo-viewer title="После обработки" :img="mosaicUrl">
          <template slot="actions">
            <a :href="mosaicUrl" target="_blank" class="card-footer-item">Open in new tab</a>
            <a href="#" class="card-footer-item">Save</a>
          </template>
        </photo-viewer>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PhotoViewer from '@/components/PhotoViewer'

export default {
  name: 'Mosaic',
  components: {
    'photo-viewer': PhotoViewer
  },
  data () {
    return {
      file: null,
      url: '',
      mosaicUrl: '',
      uploading: false
    }
  },

  methods: {
    onFileChange (e) {
      this.url = URL.createObjectURL(this.file)
      this.mosaicUrl = ''
    },

    uploadImage () {
      this.uploading = true
      let formData = new FormData()
      formData.append('file', this.file)
      axios.post('http://127.0.0.1:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(res => {
        this.mosaicUrl = 'http://127.0.0.1:5000/download/' + res.data.filename
        this.uploading = false
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

<style itemscope>
  .preview img {
    max-width: 100%;
    max-height: 720px;
  }
</style>
