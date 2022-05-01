export default {
  data() {
    return {
      height: null,
      width: null,
      oneRows: null,
      zoom: 1.5,
    };
  },
  methods: {
    resultShow() {
      // Количество кустов в одном ряду
      this.oneRows = Math.ceil(this.bushes / this.rows);
      // Ширины грядки
      this.width =
        this.rows * this.distanceBetweenRows + this.distanceBetweenRows;
      // Длины грядки
      this.height =
        this.oneRows * this.distanceBetweenBushes + this.distanceBetweenBushes;
    },
    // Рисуем
    canvasRef(refCanvas, canvasRow) {
      // Маштаб

      let сanvasEl = refCanvas; // this.$refs.canvas;
      сanvasEl.setAttribute("width", Math.ceil(this.height / this.zoom));
      // Растягиваем полотно по высоте
      сanvasEl.setAttribute("height", Math.ceil(this.width / this.zoom));
      let canvas = сanvasEl.getContext("2d");
      // Рисуем прямоугольник
      canvas.strokeRect(
        0,
        0,
        Math.ceil(this.height / this.zoom),
        Math.ceil(this.width / this.zoom)
      );
      this.canvasRow(canvas);
      setTimeout(() => {
        //this.$refs.canvasRow
        canvasRow.scrollIntoView({
          block: "start",
          behavior: "smooth",
        });
      }, 1);
    },
    // Рисует полотно под грядки
    canvasRow(canvas) {
      let l = 0;
      let iteracia = 0;
      let w = 0;
      for (let i = 1; i <= this.bushes; ++i) {
        if (this.oneRows == iteracia) {
          iteracia = 0;
          l = 0;
          w = w + this.distanceBetweenRows;
        }
        this.createImage(
          canvas,
          this.distanceBetweenRows + w,
          this.distanceBetweenBushes + l
        );
        l = l + this.distanceBetweenBushes;
        ++iteracia;
      }
    },
    createImage(canvas, r, l) {
      l = l / this.zoom;
      r = r / this.zoom;
      var circle = new Path2D();
      //circle.moveTo(125, 35);
      circle.arc(l, r, 2, 0, 2 * Math.PI);
      canvas.fill(circle);
    },
  },
};
