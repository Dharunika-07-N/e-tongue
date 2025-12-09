// Helper to create sample JSON files for spectra upload

export const createSampleSpectraFile = (type: string, herbName: string, batchNo: string) => {
  const baseData = {
    sample_id: `HERB-2025-${Math.floor(Math.random() * 1000)}`,
    herb_name: herbName,
    batch_no: batchNo,
    date_received: new Date().toISOString().split("T")[0],
    upload_info: {
      uploaded_by: "Test User",
      device_id: "ETNG-001-AI",
      raw_data_file: `${herbName.toLowerCase().replace(/\s+/g, "_")}_${type}_raw.json`,
    },
    taste_profile: {
      sweet: Math.random() * 0.3,
      sour: Math.random() * 0.4,
      salty: Math.random() * 0.2,
      bitter: Math.random() * 0.9,
      pungent: Math.random() * 0.8,
      astringent: Math.random() * 0.5,
    },
    realtime_sensor_readings: Array.from({ length: 20 }, (_, i) => ({
      time: i,
      voltage: 0.2 + Math.random() * 0.5,
    })),
    phytochemicals: {
      flavonoids: 15 + Math.random() * 15,
      polyphenols: 8 + Math.random() * 10,
      terpenoids: 5 + Math.random() * 8,
      alkaloids: 2 + Math.random() * 5,
    },
    ai_predictions: {
      rasa_classification: "Katu + Tikta (Pungent + Bitter)",
      probability: 0.85 + Math.random() * 0.1,
      detected_adulteration: Math.random() > 0.8,
      adulteration_score: Math.random() * 0.1,
    },
    quality_assessment: {
      overall_quality_score: 75 + Math.random() * 20,
      grade: ["A", "B", "C"][Math.floor(Math.random() * 3)],
      comments: "Sample data for testing purposes.",
    },
  };

  // Add type-specific spectral data
  switch (type) {
    case "ftir":
      return {
        ...baseData,
        spectral_data: {
          wavenumber: Array.from({ length: 100 }, (_, i) => 4000 - i * 35),
          absorbance: Array.from({ length: 100 }, () => Math.random() * 0.9),
        },
      };
    case "nir":
      return {
        ...baseData,
        spectral_data: {
          wavelength: Array.from({ length: 100 }, (_, i) => 800 + i * 7),
          reflectance: Array.from({ length: 100 }, () => 0.5 + Math.random() * 0.4),
        },
      };
    case "raman":
      return {
        ...baseData,
        spectral_data: {
          shift: Array.from({ length: 100 }, (_, i) => 200 + i * 15),
          intensity: Array.from({ length: 100 }, () => Math.random() * 500),
        },
      };
    default:
      return baseData;
  }
};

