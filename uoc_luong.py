import pandas as pd
import numpy as np
from scipy.stats import t, norm, chi2

# Định nghĩa hàm ướng lượng khoảng tin cậy cho trung bình khi đã biết phương sai
def calculate_confidence_interval_known_variance(data, confidence_level):
    sample_mean = np.mean(data)
    sample_size = len(data)
    z_score = norm.ppf(1 - (1 - confidence_level) / 2)
    margin_of_error = z_score * np.sqrt(np.var(data) / sample_size)
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound

# Định nghĩa hàm ướng lượng khoảng tin cậy cho trung bình khi chưa biết phương sai
def calculate_confidence_interval_unknown_variance(data, confidence_level):
    sample_mean = np.mean(data)
    sample_size = len(data)
    t_score = t.ppf(1 - (1 - confidence_level) / 2, sample_size - 1)
    margin_of_error = t_score * np.sqrt(np.var(data, ddof=1) / sample_size)
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound

## Định nghĩa hàm ước lượng khoảng tin cậy cho phương sai của phân phối chuẩn
def calculate_confidence_interval_normal_distribution(data, confidence_level):
    sample_mean = np.mean(data)
    sample_size = len(data)
    z_score = norm.ppf(1 - (1 - confidence_level) / 2)
    margin_of_error = z_score * np.sqrt(np.var(data) / sample_size)
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound

# Định nghĩa hàm ước lượng khoảng tin cậy cho tỉ lệ tổng thể
def calculate_confidence_interval_population_proportion(data, confidence_level):
    sample_size = len(data)
    sample_proportion = np.mean(data)
    z_score = norm.ppf(1 - (1 - confidence_level) / 2)
    margin_of_error = z_score * np.sqrt(abs((sample_proportion * (1 - sample_proportion)) / sample_size))
    lower_bound = sample_proportion - margin_of_error
    upper_bound = sample_proportion + margin_of_error
    return lower_bound, upper_bound

def main():
    # Đường dẫn và tên file Excel
    path = r"C:/Users/DELL/Học tập AI k3/Học kỳ II/Phân tích dữ liệu Python/"
    file_name = "Temperature.xlsx"

    # Đọc dữ liệu từ file Excel
    df = pd.read_excel(path + file_name)

    # Lấy cột dữ liệu cần ước lượng
    data = df['Temperature']

    # Tính khoảng tin cậy cho trung bình đã biết phương sai
    confidence_level = 0.95      
    lower_bound_known_variance, upper_bound_known_variance = calculate_confidence_interval_known_variance(data, confidence_level)
    print("Ước lượng khoảng tin cậy cho trung bình (Đã biết phương sai):", lower_bound_known_variance, "-", upper_bound_known_variance)

    # Tính khoảng tin cậy cho trung bình chưa biết phương sai
    lower_bound_unknown_variance, upper_bound_unknown_variance = calculate_confidence_interval_unknown_variance(data, confidence_level)
    print("Ước lượng khoảng tin cậy cho trung bình (Chưa biết phương sai):", lower_bound_unknown_variance, "-", upper_bound_unknown_variance)

    # Tính khoảng tin cậy cho phương sai của phân phối chuẩn
    sample_variance = np.var(data, ddof=1)
    sample_size = len(data)
    chi_squared_low = chi2.ppf((1 - confidence_level) / 2, sample_size - 1)
    chi_squared_high = chi2.ppf((1 + confidence_level) / 2, sample_size - 1)
    lower_bound_variance = (sample_size - 1) * sample_variance / chi_squared_high
    upper_bound_variance = (sample_size - 1) * sample_variance / chi_squared_low
    print("Ước lượng khoảng tin cậy cho phương sai (Phân phối chuẩn):", lower_bound_variance, "-", upper_bound_variance)

    # Tính khoảng tin cậy cho tỉ lệ tổng thể
    data_binary = df['Temperature']  # Cột dữ liệu nhị phân (0 hoặc 1)
    lower_bound_proportion, upper_bound_proportion = calculate_confidence_interval_population_proportion(data_binary, confidence_level)
    print("Ước lượng khoảng tin cậy cho tỉ lệ tổng thể:", lower_bound_proportion, "-", upper_bound_proportion)

if __name__ == '__main__':
    main()
