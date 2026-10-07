const floatParticles = [];
const burstParticles = [];
const FLOAT_COUNT = 140;
for (let i = 0; i < FLOAT_COUNT; i++) {
    const p = new Particle(
        Math.random() * width, Math.random() * height, "float");
        p.life = Math.random() * p.maxlife; // stagger starting life
        floatParticles.push(p);
}
function spawnHeartBurst(x, y) {
    const count = 140;
    for (let  i = 0; i < count; i++) {
        burstParticles.push(new Particle(x, y, "burst"));
    }
}
