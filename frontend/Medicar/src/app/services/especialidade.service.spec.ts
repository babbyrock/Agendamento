/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { EspecialidadeService } from './especialidade.service';

describe('Service: Especialidade', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [EspecialidadeService]
    });
  });

  it('should ...', inject([EspecialidadeService], (service: EspecialidadeService) => {
    expect(service).toBeTruthy();
  }));
});
