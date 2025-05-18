import unittest
from unittest.mock import patch, Mock
from utils.extract import extract_data_from_page
from requests.exceptions import RequestException

class TestExtract(unittest.TestCase):

    @patch('utils.extract.requests.get')
    def test_extract_data_berhasil(self, mock_get):
        html_sample = '''
        <div class="collection-card">
            <h3 class="product-title">Baju Keren</h3>
            <div class="price-container">100.00</div>
            <p>Rating: 4.5</p>
            <p>Colors: 3</p>
            <p>Size: L</p>
            <p>Gender: Male</p>
        </div>
        '''
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = html_sample
        mock_get.return_value = mock_response

        hasil = extract_data_from_page("http://dummy-url")
        self.assertIsInstance(hasil, list)
        self.assertEqual(len(hasil), 1)
        self.assertEqual(hasil[0]['title'], 'Baju Keren')

    @patch('utils.extract.requests.get')
    def test_extract_data_gagal_request(self, mock_get):
        mock_get.side_effect = RequestException("Connection error")

        with self.assertRaises(Exception) as context:
            extract_data_from_page("http://dummy-url")

        self.assertIn('Gagal mengakses', str(context.exception))

    @patch('utils.extract.requests.get')
    def test_extract_data_tanpa_produk(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '<html><body>No products here!</body></html>'
        mock_get.return_value = mock_response

        hasil = extract_data_from_page("http://dummy-url")
        self.assertIsInstance(hasil, list)
        self.assertEqual(len(hasil), 0)

if __name__ == '__main__':
    unittest.main()
