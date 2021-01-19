import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    scene: ''
  },
  getters: {
    scene: (state) => {
      return state.scene
    }
  },
  mutations: {
    setScene: (state, scene) => {
      state.scene = scene
    },
    addMesh: (state, mesh) => {
      state.scene.add(mesh)
    }
  },
  actions: {
    setScene: ({ commit }, scene) => {
      commit('setScene', scene)
    },
    addMesh: ({ commit }, mesh) => {
      commit('addMesh', mesh)
    }
  },
  modules: {
  }
})
