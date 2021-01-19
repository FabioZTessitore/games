<template>
  <div class="home">
    Home
    <button @click="addCube" v-if="!done">Add the Cube</button>

    <app-scene></app-scene>
  </div>
</template>

<script>
import SceneComponent from '@/components/Scene.vue'

import { mapActions } from 'vuex'

import { BoxGeometry, MeshNormalMaterial, Mesh } from 'three'

export default {
  name: 'Home',

  data () {
    return {
      done: false
    }
  },

  methods: {
    ...mapActions([
      'addMesh'
    ]),

    addCube () {
      var geometry = new BoxGeometry()
      var material = new MeshNormalMaterial()
      var cube = new Mesh(geometry, material)
      cube.update = function (t) {
        this.rotation.x = t;
        this.rotation.y = 2*t;
      }
      this.addMesh(cube)
      this.done = true
    }
  },

  components: {
    appScene: SceneComponent
  }
}
</script>
