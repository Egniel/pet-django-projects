<template>
    <div>
      <div id="particles-js">
      </div>
        <b-row align-v="center">
        <b-col
        cols="6"
        offset="3"
        align-v="center"
        >
        <div class="test-div ">
        </div>
        </b-col>
    </b-row>
      <div class="count-particles"> <span class="js-count-particles">--</span> particles </div>
    </div>
</template>

<script>
/*eslint-disable */
import Stats from 'stats-js';

require('particles.js');

export default {
  mounted() {
    this.$nextTick(() => {
      this.initParticleJS()
    })
  },
  methods: {
    initParticleJS () {
      particlesJS('particles-js', {
        particles: {
          number: {
            value: 80,
            density: {
              enable: true,
              value_area: 700,
            },
          },
          color: {
            value: '#ffffff',
          },
          shape: {
            type: 'circle',
            stroke: {
              width: 0,
              color: '#000000',
            },
            polygon: {
              nb_sides: 5,
            },
            image: {
              src: 'img/github.svg',
              width: 100,
              height: 100,
            },
          },
          opacity: {
            value: 0.5,
            random: false,
            anim: {
              enable: false,
              speed: 2.5986470793643046,
              opacity_min: 0.1,
              sync: false,
            },
          },
          size: {
            value: 0,
            random: false,
            anim: {
              enable: false,
              speed: 175.02497502497502,
              size_min: 26.373626373626376,
              sync: false,
            },
          },
          line_linked: {
            enable: true,
            distance: 150,
            color: '#000000',
            opacity: 0.8,
            width: 1.2,
          },
          move: {
            enable: true,
            speed: 1.5,
            direction: 'none',
            random: false,
            straight: false,
            out_mode: 'out',
            bounce: false,
            attract: {
              enable: false,
              rotateX: 600,
              rotateY: 1200,
            },
          },
        },
        interactivity: {
          detect_on: 'canvas',
          events: {
            onhover: {
              enable: false,
              mode: 'repulse',
            },
            onclick: {
              enable: true,
              mode: 'repulse',
            },
            resize: true,
          },
          modes: {
            grab: {
              distance: 400,
              line_linked: {
                opacity: 1,
              },
            },
            bubble: {
              distance: 400,
              size: 40,
              duration: 2,
              opacity: 8,
              speed: 3,
            },
            repulse: {
              distance: 200,
              duration: 0.4,
            },
            push: {
              particles_nb: 4,
            },
            remove: {
              particles_nb: 2,
            },
          },
        },
        retina_detect: true,
      });
      var count_particles, stats, update;
      stats = new Stats;
      stats.setMode(0);
      stats.domElement.style.position = 'absolute';
      stats.domElement.style.left = '0px';
      stats.domElement.style.top = '0px';
      document.body.appendChild(stats.domElement);
      count_particles = document.querySelector('.js-count-particles');
      update = () => {
        stats.begin();
        stats.end();
        if (window.pJSDom[0].pJS.particles && window.pJSDom[0].pJS.particles.array) {
          count_particles.innerText = window.pJSDom[0].pJS.particles.array.length;
        }
        requestAnimationFrame(update);
      };
      requestAnimationFrame(update);
    },
  },
};
</script>

<style scoped>
canvas {
  display: block;
}
/* ---- particles.js container ---- */
#particles-js {
  overflow: hidden;
  position: absolute;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #b3bbd7;
  background-image: url('');
  background-repeat: no-repeat;
  background-size: cover;
  background-position: 50% 50%;
}

/* ---- stats.js ---- */
.count-particles {
   background: #000022;
    position: absolute;
    top: 48px;
    left: 0;
    width: 80px;
    color: #13E8E9;
    font-size: .8em;
    text-align: left;
    text-indent: 4px;
    line-height: 14px;
    padding-bottom: 2px;
    font-family: Helvetica, Arial, sans-serif;
    font-weight: bold;
}
.js-count-particles { font-size: 1.1em;
}
#stats, .count-particles { -webkit-user-select: none;
    margin-top: 5px;
    margin-left: 5px;
}
#stats { border-radius: 3px 3px 0 0;
    overflow: hidden;
}
.count-particles { border-radius: 0 0 3px 3px;
}

.asd {
    margin-top: auto;
    margin-bottom: auto;
}
.test-div {
  font-size: 2em;
  /* display: block; */
  background: rgba(255, 255
  , 255, 0.5);
  height: 50vh;
  border-radius: 8px;
  /* filter: blur(10px); */
  /* -webkit-filter: blur(10px); */
}
</style>
