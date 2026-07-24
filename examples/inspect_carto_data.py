from pathlib import Path

from pyceps import CartoStudy


DATASET = Path(
    r"tests\Export_VT-dummy-02_14_2024-11-23-36.zip"
)

study = CartoStudy(str(DATASET))
study.import_study()
study.import_maps(study.mapNames)

print(f"Study: {study.name}")
print(f"Maps: {study.mapNames}")
print()

for map_name, ep_map in study.maps.items():
    points = ep_map.points

    n_point_ecg = sum(len(point.ecg) > 0 for point in points)
    n_point_egm = sum(len(point.egm) > 0 for point in points)

    try:
        n_map_ecg = len(ep_map.bsecg)
    except TypeError:
        n_map_ecg = 0

    print(f"Map: {map_name}")
    print(f"  Mapping points:          {len(points)}")
    print(f"  Points containing EGM:  {n_point_egm}")
    print(f"  Points containing ECG:  {n_point_ecg}")
    print(f"  Map-level ECG traces:   {n_map_ecg}")

    point_with_egm = next(
        (point for point in points if len(point.egm) > 0),
        None,
    )
    if point_with_egm is not None:
        print(f"  Example EGM point:      {point_with_egm.name}")
        print(
            "  EGM channels:           "
            f"{[trace.name for trace in point_with_egm.egm]}"
        )

    point_with_ecg = next(
        (point for point in points if len(point.ecg) > 0),
        None,
    )
    if point_with_ecg is not None:
        print(f"  Example ECG point:      {point_with_ecg.name}")
        print(
            "  ECG channels:           "
            f"{[trace.name for trace in point_with_ecg.ecg]}"
        )

    print()