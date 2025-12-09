// Sample data for testing the application

export const sampleSensorData = {
  sensor_id: "demo-01",
  values: [123, 256, 301, 220, 180, 90],
};

export const sampleHerbs = [
  {
    herb_name: "Tulsi (Ocimum sanctum)",
    batch_no: "BCH-9712",
    supplier: "Herbal Suppliers Inc.",
    spectra_type: "ftir",
  },
  {
    herb_name: "Ashwagandha (Withania somnifera)",
    batch_no: "BCH-9713",
    supplier: "Ayurvedic Herbs Co.",
    spectra_type: "nir",
  },
  {
    herb_name: "Turmeric (Curcuma longa)",
    batch_no: "BCH-9714",
    supplier: "Spice Traders Ltd.",
    spectra_type: "raman",
  },
  {
    herb_name: "Ginger (Zingiber officinale)",
    batch_no: "BCH-9715",
    supplier: "Organic Farms",
    spectra_type: "hptlc",
  },
  {
    herb_name: "Neem (Azadirachta indica)",
    batch_no: "BCH-9716",
    supplier: "Natural Products Inc.",
    spectra_type: "lcms",
  },
];

export const sampleSpectraData = {
  ftir: {
    wavenumber: [4000, 3500, 3000, 2500, 2000, 1500, 1000, 500],
    absorbance: [0.1, 0.15, 0.22, 0.35, 0.45, 0.62, 0.78, 0.85],
  },
  nir: {
    wavelength: [800, 900, 1000, 1100, 1200, 1300, 1400, 1500],
    reflectance: [0.85, 0.82, 0.78, 0.75, 0.72, 0.68, 0.65, 0.62],
  },
  raman: {
    shift: [200, 400, 600, 800, 1000, 1200, 1400, 1600],
    intensity: [120, 180, 250, 320, 380, 420, 450, 480],
  },
};

export const sampleInferenceRequest = {
  sensor: {
    values: [123, 256, 301, 220, 180, 90],
  },
  spectra: [
    0.1, 0.15, 0.22, 0.35, 0.45, 0.62, 0.78, 0.85, 0.82, 0.75, 0.72, 0.68,
    0.65, 0.62, 0.58, 0.55,
  ],
  herb_name: "Tulsi (Ocimum sanctum)",
  batch_no: "BCH-9712",
  supplier: "Herbal Suppliers Inc.",
};

