import sys
import math

magic_phrase = input()

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

zones = [" "] * 30
zone_index = 0
answer = []


def change_letter(current_letter, target_letter):
    current_index = alphabet.index(current_letter)
    target_index = alphabet.index(target_letter)

    plus_distance = (target_index - current_index) % len(alphabet)
    minus_distance = (current_index - target_index) % len(alphabet)

    if plus_distance <= minus_distance:
        return "+" * plus_distance
    return "-" * minus_distance


def move_to_zone(current_zone, target_zone):
    right_distance = (target_zone - current_zone) % len(zones)
    left_distance = (current_zone - target_zone) % len(zones)

    if right_distance <= left_distance:
        return ">" * right_distance
    return "<" * left_distance


def choose_best_zone(target_letter):
    best_zone = zone_index
    best_move = ""
    best_change = change_letter(zones[zone_index], target_letter)
    best_cost = len(best_change)

    for candidate_zone in range(len(zones)):
        move = move_to_zone(zone_index, candidate_zone)
        change = change_letter(zones[candidate_zone], target_letter)
        cost = len(move) + len(change)

        if cost < best_cost:
            best_zone = candidate_zone
            best_move = move
            best_change = change
            best_cost = cost

    return best_zone, best_move, best_change


i = 0
while i < len(magic_phrase):
    letter = magic_phrase[i]
    repeat = 1

    while i + repeat < len(magic_phrase) and magic_phrase[i + repeat] == letter:
        repeat += 1

    best_zone, move, change = choose_best_zone(letter)
    answer.append(move)
    zone_index = best_zone

    answer.append(change)
    zones[zone_index] = letter

    remaining = repeat

    if repeat >= 18:
        helper_index = (zone_index + 1) % 30
        answer.append(">")
        zone_index = helper_index

        while remaining >= 18:
            chunk = min(26, remaining)
            counter_letter = alphabet[chunk]
            answer.append(change_letter(zones[zone_index], counter_letter))
            zones[zone_index] = counter_letter
            answer.append("[<.>-]")
            zones[zone_index] = " "
            remaining -= chunk

        if remaining > 0:
            answer.append("<")
            zone_index = (zone_index - 1) % 30
            answer.append("." * remaining)
    else:
        answer.append("." * repeat)

    i += repeat

print("".join(answer))
