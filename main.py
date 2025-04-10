
import random
import time

# 수감자 전체 정보
characters = {
    "이상": {"ego": "오감도", "quote": "이상이 무엇이라 생각하시오.", "atk": 3, "coin": 2},
    "파우스트": {"ego": "표상 방출기", "quote": "모든 결과들은 파우스트가 알아요.", "atk": 3, "coin": 2},
    "돈키호테": {"ego": "라 샹그레 데 산쵸", "quote": "달려라 로시난테! 정의는 승리한다!", "atk": 3, "coin": 2},
    "료슈": {"ego": "삼라염상", "quote": "모.불.아.위.", "atk": 3, "coin": 2},
    "뫼르소": {"ego": "타인의 사슬", "quote": "수많은 것들이 옥죄어 온다…", "atk": 3, "coin": 2},
    "홍루": {"ego": "허환경", "quote": "환상의 세계로 들어가 보죠.", "atk": 3, "coin": 2},
    "히스클리프": {"ego": "시체자루", "quote": "너도… 이 안에 담아주지!", "atk": 3, "coin": 2},
    "이스마엘": {"ego": "작살박이", "quote": "그 자식은… 아직 살아있을 거야.", "atk": 3, "coin": 2},
    "로쟈": {"ego": "던져지는 것", "quote": "모든 걸 거둬들일 수는 없었어…", "atk": 3, "coin": 2},
    "싱클레어": {"ego": "지식나무의 가지", "quote": "나의 손으로 잘라낼 수 있다면…", "atk": 3, "coin": 2},
    "오티스": {"ego": "토 파토스 마토스", "quote": "여행엔 목적이 있었지…", "atk": 3, "coin": 2},
    "그레고르": {"ego": "어느 날 갑자기.", "quote": "내 팔은… 변해있었어.", "atk": 3, "coin": 2},
}

def angela_say(text):
    print(f"\n[AI 앤젤라]: {text}")
    time.sleep(1.2)

def toss_coins(base_attack, coin_count):
    return [base_attack + random.choice([-1, 0, 1]) for _ in range(coin_count)]

def activate_ego(name, ego_name, quote):
    angela_say(f"{name}의 에고 '{ego_name}'이 발동됩니다.")
    print(f">>> {quote}")

def main():
    angela_say("Limbus TRPG 시뮬레이션을 시작합니다.")
    name = random.choice(list(characters.keys()))
    data = characters[name]
    angela_say(f"이번 시뮬레이션의 대상은 수감자 '{name}'입니다.")

    print(f"\n{name}의 공격을 준비합니다...")
    results = toss_coins(data["atk"], data["coin"])
    print(f"코인 결과: {results}")
    print(f"총 피해량: {sum(results)}")

    if sum(results) >= 6:
        activate_ego(name, data["ego"], data["quote"])
    else:
        angela_say("에고 발동 조건이 충족되지 않았습니다.")

    angela_say("시뮬레이션 종료. 다음 실행을 기다립니다.")

if __name__ == "__main__":
    main()
