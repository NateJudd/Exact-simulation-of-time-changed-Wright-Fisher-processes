# merge_EWF_pngs.R
# Purpose: Read existing PNG plots and merge into a 2x2 grid image

# ---- Load required packages ----
if (!requireNamespace("png", quietly = TRUE)) install.packages("png")
if (!requireNamespace("grid", quietly = TRUE)) install.packages("grid")
if (!requireNamespace("gridExtra", quietly = TRUE)) install.packages("gridExtra")

library(png)
library(grid)
library(gridExtra)

setwd("C:/Users/User/Documents/TWF_26/sWF")

out_file_1 <- "sWF_half_half_tf.png"
out_file_2 <- "sWF_one_one_tf.png"

# ---- List of input PNGs (adjust filenames if needed) ----


png_files_1 <- c(
  "EWF_diffusion_all_times_1,1,N2.png",
  "EWF_diffusion_all_times_1,1,A2.png",
  "EWF_diffusion_all_times_1,1,G2.png",
  "EWF_diffusion_all_times_1,1,T2.png"
)

png_files_2 <- c(
  "EWF_diffusion_all_times_0.5,0.5,N1.png",
  "EWF_diffusion_all_times_0.5,0.5,A1.png",
  "EWF_diffusion_all_times_0.5,0.5,G1.png",
  "EWF_diffusion_all_times_0.5,0.5,T1.png"
)


# ---- Read images ----
images <- lapply(png_files_1, function(f) {
  if (!file.exists(f)) stop(paste("File not found:", f))
  rasterGrob(readPNG(f), interpolate = TRUE)
})

# ---- Combine into 2x2 grid ----
combined <- grid.arrange(
  grobs = images,
  nrow = 2, ncol = 2#,
  #top = textGrob("EWF Diffusion Simulation Results", gp = gpar(fontsize = 18, fontface = "bold"))
)

# ---- Save combined plot as PNG ----
png(filename = out_file_1, width = 2000, height = 1800, res = 1080)
grid.arrange(
  grobs = images,
  nrow = 2, ncol = 2#,
  #top = textGrob("EWF Diffusion Simulation Results", gp = gpar(fontsize = 18, fontface = "bold"))
)
dev.off()

images <- lapply(png_files_2, function(f) {
  if (!file.exists(f)) stop(paste("File not found:", f))
  rasterGrob(readPNG(f), interpolate = TRUE)
})

# ---- Combine into 2x2 grid ----
combined <- grid.arrange(
  grobs = images,
  nrow = 2, ncol = 2#,
  #top = textGrob("EWF Diffusion Simulation Results", gp = gpar(fontsize = 18, fontface = "bold"))
)

# ---- Save combined plot as PNG ----
png(filename = out_file_2, width = 2000, height = 1800, res = 1080)
grid.arrange(
  grobs = images,
  nrow = 2, ncol = 2#,
  #top = textGrob("EWF Diffusion Simulation Results", gp = gpar(fontsize = 18, fontface = "bold"))
)
dev.off()


cat("✅ Combined image saved as:", out_file, "\n")

