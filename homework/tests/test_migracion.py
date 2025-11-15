import os



def test_migracion():
    from ..src.wordcount import main
    
    main()

    if not os.path.exists("data/output/results.tsv"):
        raise FileNotFoundError("El archivo results.tsv no existe.")


    results = {}
    with open("data/output/results.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            key, value = line.strip().split("\t")
            results[key] = value


    assert results["computational"] == "3"
    assert results["analytics"] == "5"