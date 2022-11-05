window.onload = function () {
  Particles.init({
    selector: ".background"
  });
};
const particles = Particles.init({
  selector: ".background",
  color: ["#03dac6", "#ff0266", "#000000"],
  connectParticles: true,
  responsive: [
    {
      breakpoint: 768,
      options: {
        color: ["#faebd7", "#03dac6", "#ff0266"],
        maxParticles: 50,
        connectParticles: true,
        move: false,
      }
    }
  ]
});

// Not bad, Now you have 3rd flag: ctf{7eadb6fb4c0d9da4310e441f655af3e5} 
// Next Hint: May the next flag can be obtained by console logs of this website.