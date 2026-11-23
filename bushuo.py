"""布朔（BUSHUO）· 基线灰度分发、分批热更

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：基线灰度分发、分批热更。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Bushuo:
    """布朔（BUSHUO）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "BUSHUO"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.releases = {}
        self._seq = 0

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "bushuo",
            "cn": "布朔",
            "code": self.CODE,
            "duty": "基线灰度分发、分批热更",
            "mingwen": "朔序颁行，不骤而化",
            "anchor": self.ANCHOR,
        }

    def release(self, version, cohort):
        """朔序颁行：按批灰度分发新基线，首批即行。"""
        if not cohort:
            raise ValueError("颁行需有批次")
        self._seq += 1
        rid = "BS-%04d" % self._seq
        batches = [{"batch": str(b), "status": "active" if i == 0 else "pending"} for i, b in enumerate(cohort)]
        self.releases[version] = {"release_id": rid, "version": version, "batches": batches}
        self.events.append({"event": "release", "version": version, "batches": len(batches)})
        return rid

    def status(self, version):
        """查询颁行批次进度。"""
        if version not in self.releases:
            raise KeyError("无此版本： %s" % version)
        rel = self.releases[version]
        done = sum(1 for b in rel["batches"] if b["status"] != "pending")
        state = "done" if done == len(rel["batches"]) else "rolling"
        return {"version": version, "batches_total": len(rel["batches"]), "batches_done": done, "state": state}
