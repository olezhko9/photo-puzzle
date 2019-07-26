<template>
  <div class="container-fluid">
    <div class="columns">

      <div class="column preview">
        <photo-card title="До обработки" :img="originalUrl" @imageLoaded="getUserImageHeight">
          <template slot="no-image">
            <b-field>
              <b-upload
                v-model="file"
                type="is-primary"
                @input="onFileChange"
                accept="image/*"
                :style="{height: fixedHeight + 'px', 'max-height': fixedHeight + 'px'}"
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
            <a class="card-footer-item" @click="reset">Close</a>
            <a class="card-footer-item" @click="uploadImage">Make mosaic</a>
          </template>
        </photo-card>
      </div>

      <div class="column preview">
        <photo-card title="После обработки" :img="mosaicUrl" :maxHeight="fixedHeight">
          <template slot="no-image">
            <img src="https://cdn.shopify.com/s/files/1/0533/2089/files/placeholder-images-image_large.png?v=1530129081"
                 alt="Placeholder image"
                 :height="fixedHeight" :width="fixedHeight"
            >
            <b-loading :is-full-page="true" :active.sync="isLoading"></b-loading>
          </template>
          <template slot="actions">
            <a :href="mosaicUrl" target="_blank" class="card-footer-item">Open in new tab</a>
            <a :href="mosaicUrl" class="card-footer-item" :download="mosaicUrl">Download</a>
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
      file: null,
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
        this.mosaicUrl = process.env.SERVER_HOST + '/download/' + res.data.filename
      }).finally(() => {
        this.isLoading = false
      })
    },

    reset () {
      this.file = null
      this.originalUrl = ''
      this.mosaicUrl = ''
      this.fixedHeight = 500
    },

    getUserImageHeight () {
      const image = document.querySelector('.user-image')
      this.fixedHeight = image.height
    }
  }
}
</script>

<style itemscope>
  .preview img {
    max-height: 600px;
    margin: 0 auto;
    display: block;
  }

  .upload {
    width: 100%;
  }

  .upload-draggable {
    width: 100%;
  }

  .upload-cta {
    margin: 15% 0;
  }
</style>
