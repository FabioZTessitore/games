<template>
    <div ref="scene" class="scene">
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

import { Scene, PerspectiveCamera, WebGLRenderer, Clock } from 'three'

export default {
    data () {
        return {
            sceneWidth: 1,
            sceneHeight: 1
        }
    },

    computed: {
        ...mapGetters([
            'scene'
        ]),

        sceneRatio () {
            return this.sceneWidth / this.sceneHeight
        }
    },

    methods: {
        ...mapActions([
            'setScene'
        ])
    },

    mounted () {
        // the canvas will have the size of the scene div
        this.sceneWidth = this.$refs.scene.clientWidth
        this.sceneHeight = this.$refs.scene.clientHeight

        var scene = new Scene()
        this.setScene(scene)
        var camera = new PerspectiveCamera(75, this.sceneRatio, 0.1, 1000)
        var renderer = new WebGLRenderer()
        renderer.setSize(this.sceneWidth, this.sceneHeight)
        this.$refs.scene.appendChild( renderer.domElement )

        camera.position.z = 5

        var clock = new Clock()

        function animate() {
            requestAnimationFrame(animate)
            var t = clock.getElapsedTime()
            scene.children.forEach(mesh => {
                mesh.update(t)
            })
            renderer.render(scene, camera)
        }
        animate()
        console.log('scene created')
    }
}
</script>

<style scoped>
.scene {
    width: 90vw;
    height: 50vh;
    margin: 0 auto;
}
</style>