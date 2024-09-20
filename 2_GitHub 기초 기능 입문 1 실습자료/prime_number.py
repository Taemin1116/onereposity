data = [41, 32, 30, 23, 24, 32, 11, 39, 24, 46, 50, 18, 41, 14, 33, 50, 38, 25,
        32, 16, 43, 19, 35, 22, 46, 43, 10, 22, 17, 47, 66, 48, 25, 43, 28, 31, 12, 25, 12, 48]
no_classes = 6  # 계급의 수(데이터를 몇 구간으로 나눌지)
unit = 1  # 최소단위


def drawTable(data, no_classes, unit):
    global frequencies
    frequencies = []  # 각 계급의 도수를 저장할 리스트

    # 데이터의 최소값과 최대값을 이용해 계급간격(구간의 크기)을 계산
    w = (max(data) - min(data)) / no_classes  # 계급간격
    w = w + 0.5  # 구간을 조금 더 넓게 조정하여 포함 범위를 맞춤

    # 출력할 테이블의 제목
    print('계급 | 계급간격    | 도수 | 상대도수   | 누적도수  | 누적상대도수  | 계급값')

    cumulative_frequency = 0  # 누적도수
    cumulative_relative_frequency = 0  # 누적상대도수

    lower_bound = min(data)  # 첫 번째 계급의 하한선을 데이터의 최소값으로 설정

    # 각 구간(계급)에 대해 반복
    for n in range(no_classes):
        # 계급의 상한선을 계산
        upper_bound = lower_bound + w

        # 해당 구간에 속하는 데이터 찾기
        class_data = []
        for x in data:
            if lower_bound <= x < upper_bound:
                class_data.append(x)

        # 도수와 상대도수 계산
        frequency = len(class_data)  # 해당 구간에 있는 데이터 개수
        frequencies.append(frequency)  # 도수를 리스트에 저장
        relative_frequency = frequency / len(data)  # 상대도수 (비율)

        # 누적도수 계산
        cumulative_frequency += frequency
        cumulative_relative_frequency += relative_frequency

        # 계급값(구간의 중간값) 계산
        class_value = (lower_bound + upper_bound) / 2

        # 테이블 출력
        print(f"{n+1:3}  | {lower_bound:.1f} ~ {upper_bound:.1f} | {frequency:4} |   {relative_frequency:.4f}   | {cumulative_frequency:4}      | {cumulative_relative_frequency:.4f}        | {class_value:.1f}")

        # 다음 구간의 하한선을 업데이트
        lower_bound = upper_bound

# 함수 실행
drawTable(data, no_classes, unit)
