<template>
  <div class="container">
    <div class="columns">
      <div class="column preview">
        <photo-card title="До обработки" :img="originalUrl" :filename="file.name" :maxHeight="fixedHeight" @imageLoaded="getUserImageHeight">
          <template slot="no-image">
            <b-field>
              <b-upload
                v-model="file"
                type="is-primary"
                @input="onFileChange"
                accept="image/*"
                drag-drop>
                <section class="section">
                  <div class="has-text-centered upload-cta">
                    <p>
                      <b-icon
                        icon="upload"
                        size="is-large">
                      </b-icon>
                    </p>
                    <p>Перетащите сюда файл,   который хотите обработать,</p>
                    <p>или нажмите, чтобы выбрать</p>
                  </div>
                </section>
              </b-upload>
            </b-field>
          </template>
          <template slot="actions">
            <b-button
              type="is-info"
              class="card-footer-item"
              @click="reset">
              Закрыть
            </b-button>
            <b-button
              type="is-info"
              class="card-footer-item"
              @click="uploadImage"
              :disabled="!originalUrl">
              Обработать
            </b-button>
          </template>
        </photo-card>
      </div>

      <div class="column preview">
        <photo-card title="После обработки" :img="mosaicUrl" :filename="filename" :maxHeight="fixedHeight">
          <template slot="no-image">
            <img src="https://cdn.shopify.com/s/files/1/0533/2089/files/placeholder-images-image_large.png?v=1530129081"
                 alt="Placeholder image"
            >
            <b-loading :is-full-page="true" :active.sync="isLoading"></b-loading>
          </template>
          <template slot="actions">
            <b-button
              type="is-info"
              class="card-footer-item"
              :disabled="!mosaicUrl"
              @click.prevent="downloadImage(mosaicUrl)">
              Скачать
            </b-button>
            <b-button
              type="is-info"
              class="card-footer-item"
              :disabled="!mosaicUrl"
              tag="a"
              target="_blank"
              :href="mosaicUrl">
              Открыть в новой вкладке
            </b-button>
          </template>
        </photo-card>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PhotoCard from '@/components/PhotoCard'

export default {
  name: 'Mosaic',
  components: {
    'photo-card': PhotoCard
  },
  data () {
    return {
      file: {
        name: ''
      },
      filename: '',
      originalUrl: '',
      mosaicUrl: '',
      fixedHeight: 500,
      isLoading: false
    }
  },

  methods: {
    onFileChange (e) {
      this.originalUrl = URL.createObjectURL(this.file)
      this.mosaicUrl = ''
    },

    uploadImage () {
      this.isLoading = true
      let formData = new FormData()
      formData.append('file', this.file)

      axios.post(process.env.SERVER_HOST + '/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(res => {
        this.filename = res.data.filename
        this.mosaicUrl = process.env.SERVER_HOST + '/download/' + res.data.filename
      }).finally(() => {
        this.isLoading = false
      })
    },

    downloadImage (url) {
      axios.get(url, { responseType: 'arraybuffer' })
        .then(response => {
          const url = window.URL.createObjectURL(new Blob([response.data]))
          const link = document.createElement('a')
          link.href = url
          link.setAttribute('download', this.filename)
          document.body.appendChild(link)
          link.click()
          document.body.removeChild(link)
        })
    },

    reset () {
      this.file = {
        name: ''
      }
      this.originalUrl = ''
      this.mosaicUrl = ''
      this.filename = ''
      this.fixedHeight = 500
    },

    getUserImageHeight () {
      const image = document.querySelector('.user-image')
      this.fixedHeight = image.height
    }
  }
}
</script>

<style>
  .preview img {
    max-height: 100%;
    margin: 0 auto;
    display: block;
  }

  .upload {
    width: 100%;
    height: 100%;
  }

  .upload-draggable {
    width: 100%;
  }

  .upload-cta {
    margin: 20% 0;
  }
</style>
