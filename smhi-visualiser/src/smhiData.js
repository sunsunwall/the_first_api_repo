// Utility to fetch and parse smhi_data.json
export async function fetchSmhiData() {
  try {
    const response = await fetch('/smhi_data.json');
    if (!response.ok) throw new Error('Failed to fetch smhi_data.json');
    return await response.json();
  } catch (error) {
    return { error: error.message };
  }
}
